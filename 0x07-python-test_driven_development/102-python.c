#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_string - Prints Python string information
 * @p: PyObject string pointer
 */
void print_python_string(PyObject *p)
{
	if (PyUnicode_Check(p))
	{
		wchar_t *wstr;
		Py_ssize_t size;

		printf("[.] string object info\n");

		if (PyUnicode_IS_COMPACT_ASCII(p))
			printf("  type: compact ascii\n");
		else
			printf("  type: compact unicode object\n");

		size = PyUnicode_GET_LENGTH(p);
		wstr = PyUnicode_AsWideCharString(p, NULL);

		printf("  length: %zd\n", size);
		printf("  value: %ls\n", wstr);

		PyMem_Free(wstr);
	}
	else
	{
		fprintf(stderr, "[.] string object info\n");
		fprintf(stderr, "  [ERROR] Invalid String Object\n");
	}
}
