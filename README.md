# Edge-Conv-implementation

This project was developed for the *Neural Network* exam, academic year 2021/2022, University of Sapienza.

This projects implements the convolutional neural network on graphs described in *Dynamic Graph CNN for Learning on Point Clouds* [1]; the network is called *Dynamic Graph Convolutional Neural Network* and it uses **EdgeConv** as its fundamental building block. The model was trained on a classification task, using the dataset ModelNet40 [2], which contains 3D scans of objects belonging to 40 different categories. The model is implemented using **Pytorch**.

<p align="center">
  <img src="/src/data_samples.png" width="1000" title="example meme" >
<p\>

Point clouds are a data structure comprised of points in a vector space. They are a very flexible data structure; for example they comprise the output of 3D data acquisition devices. By looking at the success of convolutional models in other application domains it is only natural to want to apply the same techniques to such data structures. To apply convolution the points in the data need to have a "neighboring" concept: convolution is applied via a function of a point and its neighborhood. The studied paper proposes a way to structure point clouds as graphs, this way the neighborhood of a node is the set of points connected to it in the graph.

The main aspects of article [1] are a convolution algorithm on graphs, named EdgeConv, and the idea of not keeping the structure of the graph static. EdgeConv can be written concisely as:
<p align="center">
  <img src="/src/formula.png" width="250" title="EdgeConv formula" >
<p\>

where x_i' is the value of a node after the EdgeConv layer, the square operator is an aggregation operator over the neighborhood of the node, and that should be invariant to permutations of the order of the neighboring nodes. h_theta is an operation over the values of the neighbors and the node itself: in this work it is implemented as a feed-forward network with one hidden layer.

Not keeping the graph static means that after each EdgeConv operation the connections of each node with the neighbors are recomputed: in general after each iteration the distribution of the nodes is not going to be the same as before, and by recomputing the neighborhood we can find similarities between nodes initially far away.
  
The final model is reported in the figure below: four EdgeConv blocks are stack one after the other, with residual connections from the output of each layer. A Conv1D is applied, followed by a pooling layer to flatten the results, in order to pass them to a feed-forward neural network used as a classifier. 
  
<p align="center">
  <img src="/src/model.png" width="100" title="EdgeConv formula" >
<p\>

The model reached an accuracy of 0.870. Better performances are reported in [1], but the model is quite computationally intensive and training was cut short for this reason. 

## References

### Dynamic Graph CNN for Learning on Point Clouds

[1] Yue Wang, Yongbin Sun, Ziwei Liu, Sanjay E. Sarma, Michael M. Bronstein, Justin M. Solomon [*Dynamic Graph {CNN} for Learning on Point Clouds*](http://arxiv.org/abs/1801.07829)

```
@article{DBLP:journals/corr/abs-1801-07829,
  author    = {Yue Wang and
               Yongbin Sun and
               Ziwei Liu and
               Sanjay E. Sarma and
               Michael M. Bronstein and
               Justin M. Solomon},
  title     = {Dynamic Graph {CNN} for Learning on Point Clouds},
  journal   = {CoRR},
  volume    = {abs/1801.07829},
  year      = {2018},
  url       = {http://arxiv.org/abs/1801.07829},
  eprinttype = {arXiv},
  eprint    = {1801.07829},
  timestamp = {Thu, 16 Apr 2020 07:55:10 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1801-07829.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

### 3D ShapeNets for 2.5D Object Recognition and Next-Best-View Prediction

[2] Zhirong Wu, Shuran Song, Aditya Khosla, Xiaoou Tang, Jianxiong Xiao [*3D ShapeNets for 2.5D Object Recognition and Next-Best-View Prediction*](http://arxiv.org/abs/1406.5670)

```
@article{DBLP:journals/corr/WuSKTX14,
  author    = {Zhirong Wu and
               Shuran Song and
               Aditya Khosla and
               Xiaoou Tang and
               Jianxiong Xiao},
  title     = {3D ShapeNets for 2.5D Object Recognition and Next-Best-View Prediction},
  journal   = {CoRR},
  volume    = {abs/1406.5670},
  year      = {2014},
  url       = {http://arxiv.org/abs/1406.5670},
  eprinttype = {arXiv},
  eprint    = {1406.5670},
  timestamp = {Mon, 13 Aug 2018 16:47:24 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/WuSKTX14.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```
