package com.coisini.consumer.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import com.coisini.consumer.client.TestAPIClient;

@RestController
public class TestController {
    private TestAPIClient testAPIClient;

    @Autowired
    public TestController(TestAPIClient testAPIClient) {
        this.testAPIClient = testAPIClient;
    }

    @PostMapping("/test")
    public String test(@RequestParam String username) throws Exception {
        return this.testAPIClient.test(username);
    }
    
    @GetMapping("/test")
    public String test1() throws Exception {
        return this.testAPIClient.test1();
    }
}
