LANGUAGE_ID_VS_STUBS = {
    # C (GCC 8.3.0)
    "49": """
#include <stdio.h>

int main(void) {
	// your code goes here
	return 0;
}

""",
    # C++ (GCC 8.3.0)
    "53": """
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	return 0;
}

""",
    # Go (1.13.5)
    "60": """
package main
import "fmt"

func main(){
	// your code goes here
}

""",
    # Java (OpenJDK 13.0.1)
    "62": """
import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
	}
}

""",
    # JavaScript (Node.js 12.14.0)
    "63": """
console.log("Hello World")
""",
    # Python (2.7.17)
    "70": """
def main():
    # Your code goes here
    
if __name__ == "__main__":
    main()

""",
    # Python (3.8.1)
    "71": """
def main():
    # Your code goes here
    
if __name__ == "__main__":
    main()

""",
    # Ruby (2.7.0)
    "72": """
puts "Hello World"
    """
}
