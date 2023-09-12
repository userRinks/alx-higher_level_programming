#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - check if linked list received is a palindrome
 * @head: pointer to head of linked list
 * Return:
 *      (0) if NOT palindrome
 *      (1) if palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;	/* Skips slowly (1x) */
	listint_t *fast = *head;	/* Skips fast (2x) */
	listint_t *previous = NULL;	/* Reverse list ptr */
	listint_t *temp = NULL;		/* Temp ptr */

	/* If list is empty, consider it a palindrome */
	if (*head == NULL)
		return (1);

	/* Find middle of list: */
	/* since slow reaches middle when fast reaches end */
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/* Reverse the second half of the list starting from slow->next */
	while (slow != NULL)
	{
		temp = slow->next;
		slow->next = previous;
		previous = slow;
		slow = temp;
	}

	/* Reset slow to the reversed second half and fast to the head */
	slow = previous;
	fast = *head;

	/* Compare both halves for palindrome detection */
	while (slow != NULL)
	{
		if (fast->n != slow->n)
			return (0);
		fast = fast->next;
		slow = slow->next;
	}

	return (1);
}
