
 struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
  };
 

/*
128ms, 47%
60MB, 8%
*/

// running pointers, similar to what you might do in Linked List
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (root == nullptr){
            return new TreeNode(val);
        }
        
        TreeNode* curr = root;
        TreeNode* prev = curr;
        
        // binary search
        while (curr != NULL) {
            if (val < curr->val){
                prev = curr;
                curr = curr->left;
            }
            else if (val > curr->val){
                prev = curr;
                curr = curr->right;
            }
        }
        
        // insert
        if (val < prev->val)
            prev->left = new TreeNode(val);
        else if (val > prev->val)
            prev->right = new TreeNode(val);
        
        return root;
    }
};

// recursive, more elegant but not much better performance
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        // recursive
        if (root == nullptr){
            return new TreeNode(val);
        }
        if (val < root->val){
            root->left = insertIntoBST(root->left, val);
        }
        else {
            root->right = insertIntoBST(root->right, val);
        }
        
        return root;
    }
};