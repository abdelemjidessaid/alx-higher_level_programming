#include "lists.h"

/**
 * is_palindrome - function that check if a signly linked list is a palindrome.
 * @head: pointer of pointer to the head of the singly linked list.
 * Return: 1 if it is a palindrom, 0 otherwise;
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL;
	listint_t *curr = slow, *next, *first = *head, *second = prev;

	if (!fast || !fast->next)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	while (first != NULL && second != NULL)
	{
		if (first->n != second->n)
			return (0);
		first = first->next;
		second = second->next;
	}

	prev = NULL;
	curr = slow;
	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	return (1);
}
