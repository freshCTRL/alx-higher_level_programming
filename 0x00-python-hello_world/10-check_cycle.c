#include "lists.h"

/**
 * check_cycle - Entry point
 * @list: argument to function check_cycle
 *
 * Return: 0(Success)
 */

int check_cycle(listint_t *list)
{

int i = 0;
while ((i < 20) && (list != NULL))
{
list = list->next;
i++;
}
if (i == 20)
{
return (1);
}
else
{
return (0);
}
}
