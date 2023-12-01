#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_string - Prints Python string information
 * @p: PyObject string pointer
 */
void print_python_string(PyObject *p)
{
	PyASCIIObject *ascii_obj;

	fflush(stdout);

	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	ascii_obj = (PyASCIIObject *)p;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	printf("  length: %ld\n", ascii_obj->length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &ascii_obj->length));
}

