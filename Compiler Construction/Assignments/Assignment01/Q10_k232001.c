#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

#define MAX_SYMBOLS 100
#define MAX_TOKEN_LENGTH 80
#define MAX_LINE_OCCURRENCES 30

struct KeywordEntry {
    char keywordName[MAX_TOKEN_LENGTH];
    int lineNumbers[MAX_LINE_OCCURRENCES];
    int occurrenceCount;
};

struct OperatorEntry {
    char operatorSymbol[5];
    int lineNumbers[MAX_LINE_OCCURRENCES];
    int occurrenceCount;
};

struct IdentifierEntry {
    char identifierName[MAX_TOKEN_LENGTH];
    char dataType[20];
};

struct NumberEntry {
    char numericValue[MAX_TOKEN_LENGTH];
    int lineNumbers[MAX_LINE_OCCURRENCES];
    int occurrenceCount;
};

struct KeywordEntry keywordTable[MAX_SYMBOLS];
struct OperatorEntry operatorTable[MAX_SYMBOLS];
struct IdentifierEntry identifierTable[MAX_SYMBOLS];
struct NumberEntry numberTable[MAX_SYMBOLS];

int keywordCount = 0;
int operatorCount = 0;
int identifierCount = 0;
int numberCount = 0;

char *reservedKeywords[] = {
    "int", "float", "double", "char", "void",
    "if", "else", "while", "for", "return",
    "include", "main", NULL
};

char *validOperators[] = {
    "==", "!=", "<=", ">=", "+", "-", "*", "/", "=", "<", ">", NULL
};

int isKeyword(char *word) {
    for (int index = 0; reservedKeywords[index] != NULL; index++)
        if (strcmp(word, reservedKeywords[index]) == 0)
            return 1;
    return 0;
}

int isOperator(char *symbol) {
    for (int index = 0; validOperators[index] != NULL; index++)
        if (strcmp(symbol, validOperators[index]) == 0)
            return 1;
    return 0;
}

void addKeyword(char *word, int lineNumber) {
    for (int index = 0; index < keywordCount; index++) {
        if (strcmp(keywordTable[index].keywordName, word) == 0) {
            keywordTable[index].lineNumbers[keywordTable[index].occurrenceCount++] = lineNumber;
            return;
        }
    }

    strcpy(keywordTable[keywordCount].keywordName, word);
    keywordTable[keywordCount].lineNumbers[0] = lineNumber;
    keywordTable[keywordCount].occurrenceCount = 1;
    keywordCount++;
}

void addOperator(char *symbol, int lineNumber) {
    for (int index = 0; index < operatorCount; index++) {
        if (strcmp(operatorTable[index].operatorSymbol, symbol) == 0) {
            operatorTable[index].lineNumbers[operatorTable[index].occurrenceCount++] = lineNumber;
            return;
        }
    }

    strcpy(operatorTable[operatorCount].operatorSymbol, symbol);
    operatorTable[operatorCount].lineNumbers[0] = lineNumber;
    operatorTable[operatorCount].occurrenceCount = 1;
    operatorCount++;
}

void addIdentifier(char *name, char *type) {
    for (int index = 0; index < identifierCount; index++) {
        if (strcmp(identifierTable[index].identifierName, name) == 0)
            return;
    }

    strcpy(identifierTable[identifierCount].identifierName, name);
    strcpy(identifierTable[identifierCount].dataType, type);
    identifierCount++;
}

void addNumber(char *value, int lineNumber) {
    for (int index = 0; index < numberCount; index++) {
        if (strcmp(numberTable[index].numericValue, value) == 0) {
            numberTable[index].lineNumbers[numberTable[index].occurrenceCount++] = lineNumber;
            return;
        }
    }

    strcpy(numberTable[numberCount].numericValue, value);
    numberTable[numberCount].lineNumbers[0] = lineNumber;
    numberTable[numberCount].occurrenceCount = 1;
    numberCount++;
}

void lexicalAnalyzer(char *sourceCode) {
    int position = 0;
    int currentLine = 1;
    int sourceLength = strlen(sourceCode);
    char currentDataType[20] = "";

    while (position < sourceLength) {

        if (sourceCode[position] == '\n') {
            currentLine++;
            position++;
            continue;
        }

        if (isspace(sourceCode[position])) {
            position++;
            continue;
        }

        if (sourceCode[position] == '/' && sourceCode[position+1] == '/') {
            while (position < sourceLength && sourceCode[position] != '\n')
                position++;
            continue;
        }

        if (sourceCode[position] == '/' && sourceCode[position+1] == '*') {
            position += 2;
            while (position < sourceLength) {
                if (sourceCode[position] == '*' && sourceCode[position+1] == '/') {
                    position += 2;
                    break;
                }
                if (sourceCode[position] == '\n')
                    currentLine++;
                position++;
            }
            continue;
        }

        char twoCharOperator[3] = {sourceCode[position], sourceCode[position+1], '\0'};
        if (isOperator(twoCharOperator)) {
            addOperator(twoCharOperator, currentLine);
            position += 2;
            continue;
        }

        char singleCharOperator[2] = {sourceCode[position], '\0'};
        if (isOperator(singleCharOperator)) {
            addOperator(singleCharOperator, currentLine);
            position++;
            continue;
        }

        if (isdigit(sourceCode[position])) {
            char numberBuffer[MAX_TOKEN_LENGTH] = "";
            int bufferIndex = 0;

            while (position < sourceLength &&
                  (isdigit(sourceCode[position]) || sourceCode[position] == '.')) {
                numberBuffer[bufferIndex++] = sourceCode[position++];
            }

            numberBuffer[bufferIndex] = '\0';
            addNumber(numberBuffer, currentLine);
            continue;
        }

        if (isalpha(sourceCode[position]) || sourceCode[position] == '_') {

            char identifierBuffer[MAX_TOKEN_LENGTH] = "";
            int bufferIndex = 0;

            while (position < sourceLength &&
                  (isalnum(sourceCode[position]) || sourceCode[position] == '_')) {
                identifierBuffer[bufferIndex++] = sourceCode[position++];
            }

            identifierBuffer[bufferIndex] = '\0';

            if (isKeyword(identifierBuffer)) {
                addKeyword(identifierBuffer, currentLine);
                strcpy(currentDataType, identifierBuffer);
            }
            else {
                char unknownType[] = "unknown";

                addIdentifier(
                    identifierBuffer,
                    (strlen(currentDataType) > 0) ? currentDataType : unknownType
                );

                strcpy(currentDataType, "");
            }

            continue;
        }

        position++;
    }
}

void displaySymbolTable() {

    printf("\nSYMBOL TABLE OUTPUT\n");

    printf("\nKEYWORDS:\n");
    printf("%-20s Lines\n", "Keyword");

    for (int i = 0; i < keywordCount; i++) {
        printf("%-20s ", keywordTable[i].keywordName);

        for (int j = 0; j < keywordTable[i].occurrenceCount; j++)
            printf("%d ", keywordTable[i].lineNumbers[j]);

        printf("\n");
    }

    printf("\nOPERATORS:\n");
    printf("%-10s Lines\n", "Operator");

    for (int i = 0; i < operatorCount; i++) {
        printf("%-10s ", operatorTable[i].operatorSymbol);

        for (int j = 0; j < operatorTable[i].occurrenceCount; j++)
            printf("%d ", operatorTable[i].lineNumbers[j]);

        printf("\n");
    }

    printf("\nIDENTIFIERS:\n");
    printf("%-20s Type\n", "Identifier");

    for (int i = 0; i < identifierCount; i++)
        printf("%-20s %-10s\n",
               identifierTable[i].identifierName,
               identifierTable[i].dataType);

    printf("\nNUMERIC CONSTANTS:\n");
    printf("%-10s Lines\n", "Value");

    for (int i = 0; i < numberCount; i++) {
        printf("%-10s ", numberTable[i].numericValue);

        for (int j = 0; j < numberTable[i].occurrenceCount; j++)
            printf("%d ", numberTable[i].lineNumbers[j]);

        printf("\n");
    }
}

int main() {

    char sampleProgram[] =
        "#include <stdio.h>\n"
        "int main() {\n"
        "    int num = 25;\n"
        "    float avg = 3.5;\n"
        "    int total = num + 10;\n"
        "    if (num >= 20) {\n"
        "        return 1;\n"
        "    } else {\n"
        "        return 0;\n"
        "    }\n"
        "}\n";

    printf("Symbol Table Management System\n");
    printf("Compiler Construction\n");

    printf("\nSource Code:\n%s\n", sampleProgram);

    lexicalAnalyzer(sampleProgram);
    displaySymbolTable();

    return 0;
}