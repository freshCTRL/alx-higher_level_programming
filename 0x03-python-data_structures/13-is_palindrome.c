#include "lists.h"
/**
 * is_palindrome - Entry point.
 * @head: argument to is_palindrome
 * Return: (0) Success
 */
void reverse(listint_t **head)
{
listint_t *temp = NULL, *tp1;
while (*head)
{
tp1 = (*head)->next;
(*head)->next = temp;
temp = *head;
*head = tp1;
}
*head = temp;
}
int is_palindrome(listint_t **head)
{
int a, k, i, count = 0, stop = 0;
listint_t *sp = NULL, *tp = *head, *jp = *head;
while (tp)
{
tp = tp->next;
count++;
}
if ((count == 1) || (count == 0))
return (1);
k = count / 2;
tp = *head;
for (a = 0; (a < k); a++)
tp = tp->next;
if ((count % 2) == 0)
sp = tp;
else
sp = tp->next;
reverse(&sp);
for (i = 0; ((i < k)&&(stop != 1)); i++)
{
if (jp->n == sp->n)
{
jp = jp->next;
sp = sp->next;
}
else
stop = 1;
}
if (stop == 1)
return (0);
return (1);
}
