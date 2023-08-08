#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @h: A pointer to the head of the linked list.
 * @num: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **h, int num)
{
	listint_t *nd = *h, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = num;

	if (nd == NULL || nd->n >= num)
	{
		new_node->next = nd;
		*h = new_node;
		return (new_node);
	}

	while (nd && nd->next && nd->next->n < num)
		nd = nd->next;

	new_node->next = nd->next;
	nd->next = new_node;

	return (new_node);
}

