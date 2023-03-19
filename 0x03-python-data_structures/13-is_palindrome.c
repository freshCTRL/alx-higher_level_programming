#include "lists.h"

/**
 * is_palindrome - Entry point.
 * @head: argument to is_palindrome
 *
 * Return: (0) Success
 */

int is_palindrome(listint_t **head)
{

int i, j, k, count, stop;
listint_t *front;
listint_t *rear;
listint_t *man;

count = 0;
man = *head;
while (man)
{
man = man->next;
count++;
}
count--;

i = 0;
k = count / 2;
stop = 0;
while ((i < k)&&(stop != 1))
{

front = *head;
j = 0;
while (j < i)
{
front = front->next;
j++;
}

rear = *head;
j = 0;
while (j <= count - i - 1)
{
rear = rear->next;
j++;
}

if (front->n != rear->n)
{
stop = 1;
}
else
{
i++;
}
}

if (stop == 1)
{
return (0);
}
else
{
return (1);
}
return (0);
}
