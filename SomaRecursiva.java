import java.util.Scanner;

public class SomaRecursiva {
    
    public static int soma(int n) {
       
        if (n == 0) {
            return 0;
        } else {
            return n + soma(n - 1);
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        System.out.print("Digite um número natural: ");
        int numero = in.nextInt();

        int resultado = soma(numero);
        System.out.println("A soma dos números naturais até " + numero + " é: " + resultado);
        
        in.close();
    }
}
