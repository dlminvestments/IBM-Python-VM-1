iterator = training_dataset.make_one_shot_iterator()
x, y = iterator.get_next()

model.fit(x, y, steps_per_epoch=100, epochs=10)

iterator = validation_dataset.make_one_shot_iterator()
x, y = iterator.get_next()
model.evaluate(x, y, steps=50
