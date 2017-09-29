from threading import Thread
from uuid import uuid4

from flask import Flask, jsonify, request

from Blockchain_.blockchain import Blockchain


class NodesAPI:
    @staticmethod
    def start_node(app, host, port):
        app.run(host=host, port=port)

    @staticmethod
    def add_node():
        node_identifier = str(uuid4()).replace('-', '')
        app = Flask(__name__+node_identifier)
        bc = Blockchain()

        @app.route('/nodes/register', methods=['POST'])
        def register_nodes():
            values = request.get_json()

            nodes = values.get('nodes')
            if nodes is None:
                return "Error: Please supply a valid list of nodes", 400

            for node in nodes:
                bc.register_node(node)

            response = {
                'message': 'New nodes have been added',
                'total_nodes': list(bc.nodes),
            }
            return jsonify(response), 201

        @app.route('/nodes/resolve', methods=['GET'])
        def consensus():
            replaced = bc.resolve_conflicts()

            if replaced:
                response = {
                    'message': 'Our chain was replaced',
                    'new_chain': bc.chain
                }
            else:
                response = {
                    'message': 'Our chain is authoritative',
                    'chain': bc.chain
                }

            return jsonify(response), 200

        @app.route('/mine', methods=['GET'])
        def mine():
            last_block = bc.last_block
            last_proof = last_block['proof']
            proof = bc.proof_of_work(last_proof)

            bc.add_transaction(
                sender="0",
                recipient=node_identifier,
                amount=1,
            )
            block = bc.add_block(proof)

            response = {
                'message': "New Block Forged",
                'index': block['index'],
                'transactions': block['transactions'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
            }
            return jsonify(response), 200

        @app.route('/transactions/new', methods=['POST'])
        def new_transaction():
            values = request.get_json()
            required = ['sender', 'recipient', 'amount']
            if not all(k in values for k in required):
                return 'Missing values', 400

            index = bc.add_transaction(values['sender'], values['recipient'], values['amount'])
            response = {'message': f'Transaction will be added to Block {index}'}
            return jsonify(response), 201

        @app.route('/chain', methods=['GET'])
        def full_chain():
            response = {
                'chain': bc.chain,
                'length': len(bc.chain),
            }
            return jsonify(response), 200

        @app.route('/startAllNodes', methods=['GET'])
        def start_all_nodes():
            threads = [Thread(target=NodesAPI.start_node, args=(NodesAPI.add_node(), '0.0.0.0', node[-4:])) for node in bc.nodes]
            for thread in threads:
                thread.start()

            return "Created %s Nodes" % len(threads)
        return app

if __name__ == '__main__':
    NodesAPI.start_node(NodesAPI.add_node(), host='0.0.0.0', port=5000)
