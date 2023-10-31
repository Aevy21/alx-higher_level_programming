#include "lists.h"

/**
 *check_cycle - for checking if a singly linked list has a cycle
 *@list: A pointer to the head of the singly linked list to be checked.
 *Return:1 if a cycle is detected (there is a loop).
 * otherwise 0 if no cycle is found (no loop is present).
 */
int check_cycle(struct listint_t *list)
{
	struct listint_t *slow = list;
	struct listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1); /* Cycle detected */
		}
	}

	return (0); /* No cycle found */
}
