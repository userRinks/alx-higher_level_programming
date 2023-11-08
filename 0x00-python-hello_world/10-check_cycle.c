#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 *	using Floyd Warshall's algorithm.
 * @list: pointer to the head of the list
 * Return:	(0) if there is no cycle
 *		(1) if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *one = list;
	listint_t *two = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while (two != NULL && two->next != NULL)
	{
		one = one->next;          /* Move one step */
		two = two->next->next;    /* Move two steps */

		if (one == two)
		/* If one and two meet, there is a cycle */
			return (1);
	}

	/* If one reaches the list tail, no cycle present */
	return (0);
}
