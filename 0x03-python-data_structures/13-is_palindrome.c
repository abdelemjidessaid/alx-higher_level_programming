#include "lists.h"

/**
 * reverse - function that reverses a given singly linked lists.
 * @head: pointer of pointer to the first node in the list.
 * Return: void.
 */
void reverse(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - function that check if a signly linked list is a palindrome.
 * @head: pointer of pointer to the head of the singly linked list.
 * Return: 1 if it is a palindrom, 0 otherwise;
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *tmp = *head, *pointer = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			pointer = slow->next;
			break;
		}
		if (!fast->next)
		{
			pointer = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse(&pointer);

	while (pointer && tmp)
	{
		if (tmp->n == pointer->n)
		{
			pointer = pointer->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}

	if (!pointer)
		return (1);

	return (0);
}
