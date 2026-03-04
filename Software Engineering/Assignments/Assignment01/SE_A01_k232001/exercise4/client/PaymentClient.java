package client;

import core.PaymentService;

public class PaymentClient {
    private PaymentService service;

    public PaymentClient(PaymentService service) {
        this.service = service;
    }

    public void setService(PaymentService service) {
        this.service = service;
    }

    public void makePayment(double amount) {
        System.out.println("Client initiating payment...");
        service.pay(amount);
        System.out.println("Payment completed successfully.");
    }
}
