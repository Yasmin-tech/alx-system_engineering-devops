#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

int infinite_while(void);

/**
 * main - Entry point to a  a C program that creates 5 zombie processes.
 *
 * Return: void
 */

int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{
			printf("Zombie process created, PID: %u\n", getpid());
			exit(EXIT_SUCCESS);
		}
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - run an infinite loop
 *
 * Return: void
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
