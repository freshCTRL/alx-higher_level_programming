#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - Entry point.
 * @head: argument to is_palindrome
 *
 * Return: (0) Success
 */
int is_palindrome(listint_t **head)
{
int i = 0, j;
listint_t *front, *rear, *man;

int s, k, l;
int count = 0;
man = *head;
while (man)
{
man = man->next;
count++;
}
s = count / 2;
while (i != s)
{
front = rear = *head;
for (j = 0; j < i; j++)
{
front = front->next;
}
l = i + 1;
k = count - l;
for (j = 0; j < k; j++)
{
rear = rear->next;
}
if (front->n != rear->n)
{
return (0);
}
else
{
i++;
}
}
return (1);

return (0);
}
