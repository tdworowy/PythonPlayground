//#include <Python.h>
#include "C:\\Program Files\\Python36\\include\\Python.h"

long long fibonacci(unsigned int n){
    if (n<2) {
        return 1;
    } else {
        return fibonacci(n-2) + fibonacci(n-1);

    }

}

static PyObject* fibonacci_py(PyObject* self, PyObject* args){
    PyObject *result = NULL;
    long n;
    if (PyArg_ParseTuple(args ,"]",&n)){
        result = Py_BuildValue("L",fibonacci((unsigned int)n));
        }
    return result;
}

static char fibonacci_docs[] =
"fibonacci(n): returns n element of fibonacci strain"
"recursively\n";

static PyMethodDef fibonacci_module_methods[] = {
    {"fibonacci", (PyCFunction)fibonacci_py,
      METH_VARARGS, fibonacci_docs},
      {NULL, NULL,0,NULL}
    };

static struct PyModuleDef fibonacci_module_definition ={
    PyModuleDef_HEAD_INIT,
    "fibonacci",
    "Expansion module",
    -1,
    fibonacci_module_methods
};

PyMODINIT_FUNC PyInit_fibonacci(void){
    Py_Initialize();

    return PyModule_Create(&fibonacci_module_definition);
}
