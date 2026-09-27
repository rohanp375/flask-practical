#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

#define MAX_INPUT 1024
#define MAX_ARGS 64

// Function to handle custom 'search' command
void search_file(char option, char *filename, char *pattern) {
    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        printf("Error: Cannot open file '%s'\n", filename);
        return;
    }

    char line[1024];
    int line_num = 1;
    int found = 0;

    while (fgets(line, sizeof(line), fp) != NULL) {
        if (strstr(line, pattern) != NULL) {
            printf("Line %d: %s", line_num, line);
            found = 1;

            // Option 'f': stop after first occurrence
            if (option == 'f') {
                break;
            }
        }
        line_num++;
    }

    if (!found) {
        printf("Pattern '%s' not found in %s\n", pattern, filename);
    }

    fclose(fp);
}

int main() {
    char input[MAX_INPUT];
    char *args[MAX_ARGS];

    while (1) {
        printf("myshell$ ");
        fflush(stdout);

        // Read user input
        if (fgets(input, sizeof(input), stdin) == NULL) {
            break;
        }

        // Remove trailing newline character
        input[strcspn(input, "\n")] = 0;

        // Tokenize input string
        int i = 0;
        char *token = strtok(input, " ");
        while (token != NULL && i < MAX_ARGS - 1) {
            args[i++] = token;
            token = strtok(NULL, " ");
        }
        args[i] = NULL; // Null-terminate argument list

        // Ignore empty command (user just hit enter)
        if (args[0] == NULL) {
            continue;
        }

        // Exit command
        if (strcmp(args[0], "exit") == 0 || strcmp(args[0], "quit") == 0) {
            printf("Exiting myshell...\n");
            break;
        }

        // Custom command: search
        if (strcmp(args[0], "search") == 0) {
            if (args[1] != NULL && args[2] != NULL && args[3] != NULL) {
                char mode = args[1][0];
                search_file(mode, args[2], args[3]);
            } else {
                printf("Usage: search <f|a> <filename> <pattern>\n");
            }
        } 
        // Execute external system commands
        else {
            pid_t pid = fork();

            if (pid < 0) {
                perror("Fork failed");
            } else if (pid == 0) {
                // Child Process
                if (execvp(args[0], args) == -1) {
                    printf("Command not found: %s\n", args[0]);
                }
                exit(EXIT_FAILURE);
            } else {
                // Parent Process
                wait(NULL);
            }
        }
    }

    return 0;
}
