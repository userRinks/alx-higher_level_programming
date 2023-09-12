#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - check if linked list received is a palindrome
 * @head: pointer to head of linked list
 * Return:
 *	(0) if NOT palindrome
 *	(1) if palindrome
 */

int is_palindrome(listint_t **head)
{
	/* Initialize two pointers to iterate through each node */
	listint_t *slow = *head;
	listint_t *fast = *head;

	/* If list is empty, consider it a palindrome */
	if (*head == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		/* Move slow one iteration and fast two iterations */
		slow = slow->next;
		fast = fast->next->next;
	}
	listint_t *previous = NULL;
	listint_t *temp = NULL;

	/* Reverse the second half of the list starting from 'slow->next' */
	while (slow != NULL)
	{
		temp = slow->next;
		slow->next = previous;
		previous = slow;
		slow = temp;
	}
	/* Point slow to the reversed 2nd half of the list */
	slow = previous;

	/* Compare the reversed second half with the first half */
	while (slow != NULL)
	{
		if ((*head)->n != slow->n)
			/* No match hence no palindrome */
			return (0);
		*head = (*head)->next;
		slow = slow->next;
	}

	/* If all values matched, palindrome confirmed */
	return (1);
}
