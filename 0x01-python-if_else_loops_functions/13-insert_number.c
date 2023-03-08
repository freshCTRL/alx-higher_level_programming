#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - Entry point
 * @head: argument to insert_node
 * @number: an argument, it stores the data of the inserted node
 *
 * Return: NULL(Success)
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *ins = malloc(sizeof(listint_t));
listint_t *mand = *head;
if (ins == NULL)
{
return (NULL);
}
ins->n = number;
ins->next = NULL;
if (mand != NULL)
{
int clear = 0;
int end = 0;
while ((mand->next != NULL)  && (clear != 1))
{
if (ins->n < mand->next->n)
{
if (mand->n > ins->n)
{
end = 1;
}
clear = 1;
}
else
{
mand = mand->next;
}
}
if (end != 1)
{
ins->next = mand->next;
mand->next = ins;
}
else
{
ins->next = mand;
*head = ins;
}
}
else
{
*head = ins;
}
return (NULL);
}
