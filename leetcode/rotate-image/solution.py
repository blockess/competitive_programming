class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        assert matrix
        assert len(matrix) == len(matrix[0])
        
        def swap(i1,j1,i2,j2,el):
            next_el = matrix[i2][j2]
            matrix[i2][j2] = el
            return next_el
        
        def rotate_ring(ring):
            i = j = ring
            distance = len_matrix-ring-1
            for ll in range(len_matrix-1-(2*ring)):
                j = ll+ring
                el = matrix[i][j]
                for op in ['_+', '+_', '_-', '-_']:
                    current_jump = len_matrix-1-(2*ring)
                    if op == '_+':
                        dj = min(distance,j+current_jump)
                        current_jump -= dj-j
                        di = min(distance,i+current_jump)
                    elif op == '+_':
                        di = min(distance,i+current_jump)
                        current_jump -= di-i
                        dj = max(ring,j-current_jump)
                    elif op == '_-':
                        dj = max(ring,j-current_jump)
                        current_jump -= j-dj
                        di = max(ring,i-current_jump)
                    elif op == '-_':
                        di = max(ring,i-current_jump)
                        current_jump -= i-di
                        dj = min(distance,j+current_jump)
                    el = swap(i,j,di,dj,el)
                    i = di
                    j = dj
        
        len_matrix = len(matrix[0])
        nb_ring = len_matrix//2
        
        # Rotate rings
        for ln in range(nb_ring):
            rotate_ring(ln)
