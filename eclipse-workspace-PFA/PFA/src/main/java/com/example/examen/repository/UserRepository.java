package com.example.examen.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.example.examen.models.User;

@Repository
public interface UserRepository extends CrudRepository<User, Long> {
    // Additional methods if needed
}
