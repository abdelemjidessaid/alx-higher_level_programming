#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the linked list.
 * Return: 0 if no cycle, 1 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *second = list;

	if (list == NULL)
		return (0);

	first = list->next;
	while (first && second && first->next)
	{
		if (first == second)
			return (1);
		first = first->next->next;
		second = second->next;
	}
	return (0);
}

