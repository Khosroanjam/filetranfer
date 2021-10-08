module.exports = {
    // ...your config...
    module: {
      rules: [{
        test: /\.css$/,
        use: ["style-loader", "css-loader"]
      }]
    }
  };