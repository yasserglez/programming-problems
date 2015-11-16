#include <stdio.h>
#include <stdlib.h>

void reverse(char *str)
{
  size_t str_len = 0;
  size_t i, j;
  char tmp;

  while (str[str_len] != '\0') str_len++;

  if (str_len > 0) {
    i = 0;
    j = str_len - 1;
    while (i < j) {
      tmp = str[i];
      str[i] = str[j];
      str[j] = tmp;
      i++;
      j--;
    }
  }
}


int main(void)
{
  char *buffer = NULL;
  size_t buffer_size = 0;
  ssize_t line_chars;

  while ((line_chars = getline(&buffer, &buffer_size, stdin)) != -1) {
    if (buffer[line_chars - 1] == '\n') {
      buffer[line_chars - 1] = '\0';
    }
    reverse(buffer);
    printf("%s\n", buffer);
  }

  if (buffer != NULL) free(buffer);

  return EXIT_SUCCESS;
}
