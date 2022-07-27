# project-estimator
A Project to make montecarlo estimations for projects


## Idea

Have a yaml with a tasks that must be simulated

``` yaml
- id: 1
  name: Task1
  duration : [2, 5]
  parallelization: 0.5
- id: 2
  name: Task2
  duration: 5
  parallelization: [0.5, 1.]
  predecesors: [1]
```
