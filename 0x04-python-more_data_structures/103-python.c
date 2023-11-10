#include <Python.h>

/**
 * print_python_list - Print information about a Python list
 * @p: PyObject pointer to the list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[*] Invalid Bytes Object\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

		if (PyBytes_Check(item))
		{
			printf("[.] bytes object info\n");
			printf("  size: %ld\n", PyBytes_Size(item));
			printf("  trying string: %s\n", PyBytes_AsString(item));
			printf("  first 10 bytes: ");
			for (Py_ssize_t j = 0; j < PyBytes_Size(item) && j < 10; j++)
			{
				printf("%02x ", (unsigned char)PyBytes_AsString(item)[j]);
			}
			printf("\n");
		}
	}
}

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: PyObject pointer to the bytes object
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	char *string;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[.] bytes object info\n");
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	printf("  first 10 bytes: ");
	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
		printf("%02x ", (unsigned char)string[i]);
	}
	printf("\n");
}
