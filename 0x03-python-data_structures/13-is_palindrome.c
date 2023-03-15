#include "lists.h"
/**
 * is_palindrome - Entry point.
 * @head: argument to is_palindrome
 *
 * Return: (0) Success
 */
int is_palindrome(listint_t **head)
{
listint_t *first_start;
listint_t *second_start;
listint_t *p;
listint_t *q;

p = *head;
q = *head;
if (p == NULL)
return (1);
if (p != NULL)
{
while (1)
{
p = p->next->next;
if (p == NULL)
{
second_start = q->next;
break;
}
if (p->next == NULL)
{
second_start = q->next->next;
break;
}
q = q->next;
}
q->next = NULL;
first_start = *head;
listint_t *temp2;
listint_t *temp = NULL;
while (second_start != NULL)
{
temp2 = second_start->next;
second_start->next = temp;
temp = second_start;
second_start = temp2;
}
second_start = temp;
int stop = 0;
while (first_start != NULL && stop != 1)
{
if (first_start->n == second_start->n)
{
first_start = first_start->next;
second_start = second_start->next;
}
else
stop = 1;
}
if (stop == 1)
return (0);
else
return (1);
}
return (0);
}
