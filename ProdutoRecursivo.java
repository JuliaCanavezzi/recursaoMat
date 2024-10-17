import java.util.Scanner;

public class ProdutoRecursivo {
    
    public static int produto(int a, int b) {

        if (b == 0) {
            return 0;
        }

        else if (b == 1) {
            return a;
        }

        else {
            return a + produto(a, b - 1);
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        System.out.print("Digite o primeiro número: ");
        int num1 = in.nextInt();
        
        System.out.print("Digite o segundo número: ");
        int num2 = in.nextInt();

        int resultado = produto(num1, num2);
        System.out.println("O produto de " + num1 + " e " + num2 + " é: " + resultado);

       /*System.out.println("Cálculo:");
        System.out.println(num1 + " + P (" + num1 + " * " + (num2 - 1) + ") = " + resultado);
       */ 
        in.close();
    }
}
