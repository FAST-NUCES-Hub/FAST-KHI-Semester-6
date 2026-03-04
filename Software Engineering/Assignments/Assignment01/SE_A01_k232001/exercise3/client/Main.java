package client;

import core.PaymentService;
import integration.LoggingPayIntegration;

public class Main {
    public static void main(String[] args) {
        PaymentService service = new LoggingPayIntegration();
        PaymentClient client = new PaymentClient(service);
        client.makePayment(300.0);
    }
}
