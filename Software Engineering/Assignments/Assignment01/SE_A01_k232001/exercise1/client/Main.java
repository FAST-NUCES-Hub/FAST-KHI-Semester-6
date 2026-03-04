package client;

import core.PaymentService;
import integration.CentPayIntegration;

public class Main {
    public static void main(String[] args) {
        PaymentService service = new CentPayIntegration();
        PaymentClient client = new PaymentClient(service);
        client.makePayment(99.99);
    }
}
