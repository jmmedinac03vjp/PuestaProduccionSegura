import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class Calculadora extends Application {

    private TextField num1Field = new TextField();
    private TextField num2Field = new TextField();
    private TextField resultField = new TextField();

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Calculadora");

        GridPane grid = new GridPane();
        grid.setHgap(10);
        grid.setVgap(10);

        grid.add(new Label("Número 1:"), 0, 0);
        grid.add(num1Field, 1, 0);

        grid.add(new Label("Número 2:"), 0, 1);
        grid.add(num2Field, 1, 1);

        grid.add(new Label("Resultado:"), 0, 2);
        resultField.setEditable(false);
        grid.add(resultField, 1, 2);

        Button sumaBtn = new Button("Sumar");
        sumaBtn.setOnAction(e -> calcular("+"));
        grid.add(sumaBtn, 0, 3);

        Button restaBtn = new Button("Restar");
        restaBtn.setOnAction(e -> calcular("-"));
        grid.add(restaBtn, 1, 3);

        Button multiplicacionBtn = new Button("Multiplicar");
        multiplicacionBtn.setOnAction(e -> calcular("*"));
        grid.add(multiplicacionBtn, 0, 4);

        Button divisionBtn = new Button("Dividir");
        divisionBtn.setOnAction(e -> calcular("/"));
        grid.add(divisionBtn, 1, 4);

        Scene scene = new Scene(grid, 300, 250);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private void calcular(String operacion) {
        try {
            int num1 = Integer.parseInt(num1Field.getText());
            int num2 = Integer.parseInt(num2Field.getText());
            int result = 0;

            switch (operacion) {
                case "+":
                    result = num1 + num2;
                    break;
                case "-":
                    result = num1 - num2;
                    break;
                case "*":
                    result = num1 * num2;
                    break;
                case "/":
                    if (num2 == 0) {
                        showAlert("Error", "División por cero");
                        return;
                    }
                    result = num1 / num2;
                    break;
            }

            resultField.setText(String.valueOf(result));
        } catch (NumberFormatException e) {
            showAlert("Error", "Por favor, ingrese números enteros");
        }
    }

    private void showAlert(String title, String message) {
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.setTitle(title);
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }
}
