#include "lists.h"
/**
  * check_cycle - checks if a linked list has a cycle in it.
  * @list: head of the listint_t list.
  * Return: 1 if the list has a cycle. If list is NULL, or if the list doesn't
  * have a cycle, the function returns 0.
  */
int check_cycle(listint_t *list)
{
	listint_t *temp;
	int n;

	if (list == NULL)
		return (0);
	n = 0;
	temp = list;
	while (temp != NULL)
	{
		if (check_if_recurring(list, temp, n) == 1)
			return (1);
		n++;
		temp = temp->next;
	}
	/* Not recurring */
	return (0);
}
/**
  * check_if_recurring - checks whether a pointer is recurring in a list.
  * @head: head of the listint_t list
  * @current: the pointer that is to be checked whether it is recurring.
  * @n: the index of the current pointer.
  * Return: 1 if the pointer is recurring, and 0 if either head or current is
  * NULL or if the pointer is not recurring.
  */
int check_if_recurring(listint_t *head, listint_t *current, int n)
{
	int i;
	listint_t *temp;

	if (head == NULL || current == NULL)
		return (0);
	temp = head;
	for (i = 0; i < n - 1; i++)
	{
		if (temp == current)
			return (1);
		temp = temp->next;
	}
	/* Not recurring */
	return (0);
}
