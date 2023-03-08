#include "lists.h"

/**
 * check_cycle - checks of a singly linked list has a cyle in it
 * @list: pointer to the singly linked list
 * Return: 0 if there is no cycle; 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list;

	while (current->next)
	{
		if ((current->next) == list)
			return (1);
		current = current->next;
	}
	return (0);
}
