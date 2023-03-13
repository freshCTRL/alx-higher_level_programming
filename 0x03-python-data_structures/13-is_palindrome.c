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
char mylist[50];

if (*head == 0)
{
return (1);
}
int n = 0;
while (*head)
{
mylist[n] = (*head)->n;
*head = (*head)->next;
n++;
}
n--;
int stop = 0;
int k = n - 1;
int i = 0;
while ((i <= (k / 2)) && (stop != 1))
{
if (mylist[i] != mylist[n])
{
stop = 1;
return (0);
}
else
{
if (i == (k / 2))
{
return (1);
}
}
i++;
n--;
}
return (0);
}
