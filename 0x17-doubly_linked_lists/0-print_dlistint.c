#include "lists.h"

/**
 * print_dlistint - function that prints all elements of a doubly linked list.
 * @h: pointer to the head of the doubly linked list.
 * Return: the number of nodes.
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;
	const dlistint_t *head = h;

	while (head)
	{
		if (count > 0 && head == h)
			break;
		printf("%d\n", head->n);
		head = head->next;
		count++;
	}
	return (count);
}
