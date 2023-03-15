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
if (*head == NULL)
{
return (1);
}
else
{
int count = 0;
man = *head;
while (man)
{
man = man->next;
count += 1;
}

while (i != count / 2)
{
front = rear = *head;
for (j = 0; j < i; j++)
{
front = front->next;
}
for (j = 0; j < count - (i + 1); j++)
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
}
return (1);
}
