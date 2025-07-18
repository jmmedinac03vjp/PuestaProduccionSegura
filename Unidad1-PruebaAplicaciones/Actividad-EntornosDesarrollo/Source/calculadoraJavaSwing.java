import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Calculadora extends JFrame implements ActionListener {
    private JTextField num1Field, num2Field, resultField;
    private JButton sumaBtn, restaBtn, multiplicacionBtn, divisionBtn;

    public Calculadora() {
        setTitle("Calculadora");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(null);

        JLabel num1Label = new JLabel("Número 1:");
        num1Label.setBounds(10, 10, 80, 25);
        add(num1Label);

        JLabel num2Label = new JLabel("Número 2:");
        num2Label.setBounds(10, 40, 80, 25);
        add(num2Label);

        JLabel resultLabel = new JLabel("Resultado:");
        resultLabel.setBounds(10, 70, 80, 25);
        add(resultLabel);

        num1Field = new JTextField();
        num1Field.setBounds(100, 10, 160, 25);
        add(num1Field);

        num2Field = new JTextField();
        num2Field.setBounds(100, 40, 160, 25);
        add(num2Field);

        resultField = new JTextField();
        resultField.setBounds(100, 70, 160, 25);
        resultField.setEditable(false);
        add(resultField);

        sumaBtn = new JButton("Sumar");
        sumaBtn.setBounds(10, 100, 80, 25);
        sumaBtn.addActionListener(this);
        add(sumaBtn);

        restaBtn = new JButton("Restar");
        restaBtn.setBounds(100, 100, 80, 25);
        restaBtn.addActionListener(this);
        add(restaBtn);

        multiplicacionBtn = new JButton("Multiplicar");
        multiplicacionBtn.setBounds(190, 100, 100, 25);
        multiplicacionBtn.addActionListener(this);
        add(multiplicacionBtn);

        divisionBtn = new JButton("Dividir");
        divisionBtn.setBounds(190, 130, 100, 25);
        divisionBtn.addActionListener(this);
        add(divisionBtn);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        try {
            int num1 = Integer.parseInt(num1Field.getText());
            int num2 = Integer.parseInt(num2Field.getText());
            int result = 0;

            if (e.getSource() == sumaBtn) {
                result = num1 + num2;
            } else if (e.getSource() == restaBtn) {
                result = num1 - num2;
            } else if (e.getSource() == multiplicacionBtn) {
                result = num1 * num2;
            } else if (e.getSource() == divisionBtn) {
                if (num2 == 0) {
                    JOptionPane.showMessageDialog(this, "Error: División por cero", "Error", JOptionPane.ERROR_MESSAGE);
                    return;
                }
                result = num1 / num2;
            }

            resultField.setText(String.valueOf(result));
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Por favor, ingrese números enteros", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public static void main(String[] args) {
        Calculadora calculadora = new Calculadora();
        calculadora.setVisible(true);
    }
}
