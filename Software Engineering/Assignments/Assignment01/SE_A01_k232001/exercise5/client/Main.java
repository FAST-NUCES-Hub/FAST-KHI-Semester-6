package client;

import core.PaymentService;
import integration.MockPayIntegration;

public class Main {
    public static void main(String[] args) {
        PaymentService service = new MockPayIntegration();
        PaymentClient client = new PaymentClient(service);
        client.makePayment(500.0);
    }
}
