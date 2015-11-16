#include <stdio.h>
#include <stdlib.h>

int
main(void)
{
    char *buffer = NULL;
    size_t buffer_size = 0;
    ssize_t line_chars;

    while ((line_chars = getline(&buffer, &buffer_size, stdin)) != -1) {
        if (buffer[line_chars - 1] == '\n') {
            buffer[line_chars - 1] = '\0';
        }
        printf("Hello, %s!\n", buffer);
    }

    if (buffer != NULL) free(buffer);

    return EXIT_SUCCESS;
}
