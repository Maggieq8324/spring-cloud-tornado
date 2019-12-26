package com.coisini.consumer.client;

import org.springframework.cloud.netflix.feign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import com.coisini.consumer.config.FeignConfigure;

@FeignClient(name="tornado-server", configuration = FeignConfigure.class)
public interface TestAPIClient {

    @PostMapping("/test")
    String test(@RequestParam("username") String username);
    
    @GetMapping("/test")
    String test1();
}
