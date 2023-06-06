#include "lists.h"

/**
 * insert_node - function that inserts a number into a sorted
 * linkedlist.
 * @head: pointer to the head of given linkelist.
 * @number: number of nodes that inserted.
 * Return: pointer to the new node if success, NULL otherwise.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	if (!node || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;
	new->next = node->next;
	node->next = new;
	return (new);
}

