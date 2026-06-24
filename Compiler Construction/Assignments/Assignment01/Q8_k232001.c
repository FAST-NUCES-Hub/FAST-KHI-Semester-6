#include <stdio.h>
#include <ctype.h>
#include <string.h>

int isValidVariable(char *variableName) {
    int index;
    int nameLength = strlen(variableName);

    if (nameLength == 0)
        return 0;

    if (!isalpha(variableName[0]))
        return 0;

    for (index = 1; index < nameLength; index++) {
        if (!isalpha(variableName[index]) && !isdigit(variableName[index]))
            return 0;
    }
    return 1;
}

int main() {
    char userInput[100];

    printf("Enter a variable name to check: ");
    scanf("%s", userInput);

    if (isValidVariable(userInput))
        printf("'%s' is a VALID variable name.\n", userInput);
    else
        printf("'%s' is NOT a valid variable name.\n", userInput);

    char *testVariables[] = {"Muzammil", "faheem321", "1student", "Siddiqui", "hello_world", "qwerty"};
    int totalTests = 6;

    for (int testIndex = 0; testIndex < totalTests; testIndex++) {
        if (isValidVariable(testVariables[testIndex]))
            printf("%-15s --> VALID\n", testVariables[testIndex]);
        else
            printf("%-15s --> INVALID\n", testVariables[testIndex]);
    }

    return 0;
}