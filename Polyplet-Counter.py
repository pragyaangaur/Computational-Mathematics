print("Polyplet Counter")
user_input = input("Enter target size N: ")
target_n = int(user_input) if user_input.strip() else 3

shapes = { ((0, 0),) }

directions = [
    (0, 1), (1, 0), (0, -1), (-1, 0),
    (1, 1), (1, -1), (-1, 1), (-1, -1)
]

for current_size in range(2, target_n + 1):
    next_shapes = set()
    for shape in shapes:
        for x, y in shape:
            for dx, dy in directions:
                new_block = (x + dx, y + dy)
                
                if new_block not in shape:
                    new_shape = list(shape) + [new_block]
                    
                    symmetries = [
                        [(bx, by) for bx, by in new_shape],    # Identity
                        [(-by, bx) for bx, by in new_shape],   # Rotate 90
                        [(-bx, -by) for bx, by in new_shape],  # Rotate 180
                        [(by, -bx) for bx, by in new_shape]    # Rotate 270
                    ]

                    canonical_form = None
                    
                    for sym in symmetries:
                        min_x = min(b[0] for b in sym)
                        min_y = min(b[1] for b in sym)
                        normalized_sym = tuple(sorted((b[0] - min_x, b[1] - min_y) for b in sym))
                        
                        if canonical_form is None or normalized_sym < canonical_form:
                            canonical_form = normalized_sym                            
                    next_shapes.add(canonical_form)
                    
    shapes = next_shapes

print(f"There are {len(shapes)} pseudo-polyominos of size {target_n}.")
