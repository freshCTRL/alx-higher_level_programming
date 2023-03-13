#include "lists.h"

/**
 * is_palindrome - Entry point.
 * @head: argument to is_palindrome
 *
 * Return: (0) Success
 */

int is_palindrome(listint_t **head)
{
char mylist[50];
listint_t *mand;
mand = *head;
int n = 0;
while (mand)
{
mylist[n] = mand->n;
mand = mand->next;
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
