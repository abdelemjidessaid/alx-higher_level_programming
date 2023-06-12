#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - function that prints all infro about a list
 * of python objects.
 * @p: pointer to the python list.
 * Return: void.
 */
void print_python_list_info(PyObject *p)
{
	unsigned int len, index, allocated;
	PyTypeObject *type;
	const char *name;

	if (!p)
		return;
	len = (unsigned int) PyList_Size(p);
	allocated = (unsigned int) ((PyListObject *) p)->allocated;
	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", allocated);

	for (index = 0; index < len; index++)
	{
		type = PyList_GET_ITEM(p, index)->ob_type;
		name = type->tp_name;
		printf("Element %d: %s\n", index, name);
	}
}
