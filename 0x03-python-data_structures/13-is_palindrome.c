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
listint_t *front, *rear, *man;

if ((*head == NULL) || ((*head)->next == NULL))
{
return (1);
}
count = 0;
man = *head;
while (man)
{
man = man->next;
count++;
}
i = 0;
k = count / 2;
stop = 0;
while ((i < k)&&(stop != 1))
{
j = 0;
front = *head;
while (j < i)
{
front = front->next;
j++;
}
j = 0;
rear = *head;
while (j < count - i - 1)
{
rear = rear->next;
j++;
}
if (front->n != rear->n)
stop = 1;
else
i++;

}
if (stop != 1)
return (1);

return (0);
}
