#include "lists.h"
/**
 * is_palindrome - Entry point.
 * @head: argument to is_palindrome
 *
 * Return: (0) Success
 */
int is_palindrome(listint_t **head)
{
int i, j, count, stop;
listint_t *front;
listint_t *rear;
listint_t *man;

count = 0;
man = *head;
while (man != NULL)
{
man = man->next;
count++;
}

if (*head != NULL)
{
stop = 0;
front = head;
rear = head;
while ((i != count / 2) && (stop != 1))
{
j = 0;
while (j < i)
{
front = front->next;
j++;
}

j = 0;
while (j < count - (i + 1))
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
}
return (1);
}
